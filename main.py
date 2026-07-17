"""
Filter epoched MEG/EEG data.

This app loads epoched data, applies a bandpass (and optional notch)
filter to it using the parameters specified in config.json, saves the
filtered data, and generates a QC report comparing original and
filtered data.

Inputs:
    - epo: Path to epoched MNE data (.fif)
    - l_freq, h_freq: Bandpass filter bounds
    - notch: Optional comma-separated notch filter frequencies
    - filter_length, l_trans_bandwidth, h_trans_bandwidth, method,
      iir_params, phase, fir_window, fir_design, skip_by_annotation, pad,
      picks: Parameters forwarded to mne.Epochs.filter

Outputs:
    - out_dir/epo.fif: Filtered epoched data
    - out_figs/filter_response.png: Filter frequency response plot
    - out_report/report.html: QC report comparing original and filtered data
    - product.json: Metadata about the filtering
"""

# Copyright (c) 2026 brainlife.io
#
# Author: Franco Pestilli

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

# Standard imports
import mne
import matplotlib.pyplot as plt
from mne.viz import plot_filter, plot_ideal_filter
import re

# Import shared utilities
from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_image_to_product,
    require_config_keys
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Ensure output directories exist
ensure_output_dirs('out_dir', 'out_dir_figs', 'out_dir_report')

# Load configuration
config = load_config()
require_config_keys(config, ['epo'])

# == LOAD DATA ==
fname = config['epo']
epo = mne.read_epochs(fname, preload=True)
epo_orig = epo.copy()
sfreq = epo.info['sfreq']
f = mne.filter.create_filter(epo_orig.get_data(),
                             sfreq,
                             l_freq=config['l_freq'],
                             h_freq=config['h_freq'],
                             filter_length=config['filter_length'],
                             l_trans_bandwidth=config['l_trans_bandwidth'],
                             h_trans_bandwidth=config['h_trans_bandwidth'],
                             method=config['method'],
                             iir_params=config['iir_params'],
                             phase=config['phase'],
                             fir_window=config['fir_window'],
                             fir_design=config['fir_design'])

plt.figure()
fig = plot_filter(f, sfreq)
fig_path = os.path.join('out_dir_figs', 'filter_response.png')
plt.savefig(fig_path)

if config['notch']:
    config['notch'] = [int(x) for x in re.split("\\W+", config['notch'])]
    epo.notch_filter(freqs=config['notch'], picks=config['picks'])

epo.filter(picks=config['picks'],
           l_freq=config['l_freq'],
           h_freq=config['h_freq'],
           filter_length=config['filter_length'],
           l_trans_bandwidth=config['l_trans_bandwidth'],
           h_trans_bandwidth=config['h_trans_bandwidth'],
           method=config['method'],
           iir_params=config['iir_params'],
           phase=config['phase'],
           fir_window=config['fir_window'],
           fir_design=config['fir_design'],
           skip_by_annotation=config['skip_by_annotation'],
           pad=config['pad'])

report = mne.Report(title='Filtering report')
report.add_figure(fig, title='Filter')
report.add_epochs(epo_orig, 'Original unfiltered data', psd=True)
report.add_epochs(epo, 'Filtered data', psd=True)
report.save(os.path.join('out_dir_report', 'report.html'), overwrite=True, verbose=False)

epo.save(os.path.join('out_dir', 'meg-epo.fif'), overwrite=True)

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, f'Filtered epochs: {config["l_freq"]}-{config["h_freq"]} Hz', 'success')
add_image_to_product(product_items, 'Filter response', filepath=fig_path)
create_product_json(product_items)
