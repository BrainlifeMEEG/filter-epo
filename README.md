# Filter Epoched MEG/EEG Data

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Band-pass and optionally notch-filters epoched MEG/EEG data with MNE-Python (Epochs.filter, FIR or IIR) and outputs the filtered epochs, a filter-response plot and a comparison report.**

Applies mne.Epochs.filter with the given cut-offs and filter design options to the selected channels, plus a separate notch filter at the listed frequencies, then saves the filtered epochs, a plot of the filter frequency response and an HTML report comparing original and filtered data and their spectra. Note that filtering short epochs can introduce edge artefacts; filtering continuous data first is usually preferable.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/epochs` |
| 📤 **Outputs** | `neuro/meeg/mne/epochs` · `generic/image/png` · `report/html` |
| 🐳 **Container** | `brainlifemeeg/mne:1.12.1` |
| ⚙️ **Resources** | 4 CPUs · 20 GB memory |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.758](https://doi.org/10.25663/brainlife.app.758) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif` | `neuro/meeg/mne/epochs` | yes | Epoched MEG/EEG data (MNE epochs FIF). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/epochs` | Filtered epoched data (MNE epochs FIF). |
| `out_figs` | `generic/image/png` | Frequency-response plot (PNG) of the applied filter. |
| `out_report` | `report/html` | HTML report comparing original and filtered epochs, including power spectral densities. |

<details>
<summary><b>⚙️ Parameters</b> (14)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `l_freq` | number |  | [ float \| None ] For FIR filters, the lower pass-band edge; for IIR filters, the lower cutoff frequency. If None the data are only low-passed. |
| `h_freq` | number |  | [ float \| None ] For FIR filters, the upper pass-band edge; for IIR filters, the upper cutoff frequency. If None the data are only high-passed. |
| `picks` | string |  | [ str \| array_like \| slice \| None ] Channels to include. Slices and lists of integers will be interpreted as channel indices. In lists, channel type strings (e.g., ['meg', 'eeg']) will pick channels of those types, channel name strings (e.g., ['MEG0111', 'MEG2623'] will pick the given channels. Can also be the string values “all” to pick all channels, or “data” to pick data channels. None (default) will pick all data channels. Note that channels in info['bads'] will be included if their names or indices are explicitly provided. |
| `notch` | string |  | Comma separated list of frequencies to filter out. Nota: A separate filter is applied for this purpose. |
| `filter_length` | string | `auto` | [ str \| int ] Length of the FIR filter to use (if applicable): ‘auto’ (default): The filter length is chosen based on the size of the transition regions (6.6 times the reciprocal of the shortest transition band for fir_window=’hamming’ and fir_design=”firwin2”, and half that for “firwin”). str: A human-readable time in units of “s” or “ms” (e.g., “10s” or “5500ms”) will be converted to that number of samples if phase="zero", or the shortest power-of-two length at least that duration for phase="zero-double". int: Specified length in samples. For fir_design=”firwin”, this should not be used. |
| `l_trans_bandwidth` | string |  | [ float \| str ] Width of the transition band at the low cut-off frequency in Hz (high pass or cutoff 1 in bandpass). Can be “auto” (default) to use a multiple of l_freq: min(max(l_freq * 0.25, 2), l_freq) Only used for method='fir'. |
| `h_trans_bandwidth` | string | `auto` | [ float \| str ] Width of the transition band at the high cut-off frequency in Hz (low pass or cutoff 2 in bandpass). Can be “auto” (default in 0.14) to use a multiple of h_freq: min(max(h_freq * 0.25, 2.), info['sfreq'] / 2. - h_freq) Only used for method='fir'. |
| `method` | string | `fir` | Filter implementation: 'fir' (overlap-add FIR) or 'iir' (forward-backward IIR filtering). |
| `iir_params` | string |  | [ dict \| None ] Dictionary of parameters to use for IIR filtering. If iir_params is None and method=”iir”, 4th order Butterworth will be used. For more information, see mne.filter.construct_iir_filter(). |
| `phase` | string | `zero` | [ str ] Phase of the filter, only used if method='fir'. Symmetric linear-phase FIR filters are constructed, and if phase='zero' (default), the delay of this filter is compensated for, making it non-causal. If phase='zero-double', then this filter is applied twice, once forward, and once backward (also making it non-causal). If 'minimum', then a minimum-phase filter will be constricted and applied, which is causal but has weaker stop-band suppression. |
| `fir_window` | string | `hamming` | [ str ] The window to use in FIR design, can be “hamming” (default), “hann” (default in 0.13), or “blackman”. |
| `fir_design` | string | `firwin` | [ str ] Can be “firwin” (default) to use scipy.signal.firwin(), or “firwin2” to use scipy.signal.firwin2(). “firwin” uses a time-domain design technique that generally gives improved attenuation using fewer samples than “firwin2”. |
| `skip_by_annotation` | string | `('edge', 'bad_acq_skip')` | [ str \| list of str ] If a string (or list of str), any annotation segment that begins with the given string will not be included in filtering, and segments on either side of the given excluded annotated segment will be filtered separately (i.e., as independent signals). The default (('edge', 'bad_acq_skip') will separately filter any segments that were concatenated by mne.concatenate_raws() or mne.io.Raw.append(), or separated during acquisition. To disable, provide an empty list. Only used if inst is raw. |
| `pad` | string |  | [ str ] The type of padding to use. Supports all numpy.pad() mode options. Can also be "reflect_limited", which pads with a reflected version of each vector mirrored on the first and last values of the vector, followed by zeros. Only used for method='fir'. |

</details>

📚 **References used by this App:**
- Gramfort A et al. MEG and EEG data analysis with MNE-Python. Frontiers in Neuroscience 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.758-blue.svg)](https://doi.org/10.25663/brainlife.app.758)

## Description

This Brainlife.io application filters epoched MEG/EEG data using frequency domain filtering techniques. It calls `mne.Epochs.filter()` to apply a bandpass filter (FIR or IIR) and, optionally, `mne.Epochs.notch_filter()` to remove specific frequency bands (e.g., power line noise and its harmonics). The filter frequency response used for the bandpass step is computed with `mne.filter.create_filter()` and visualized with `mne.viz.plot_filter()`.

The app generates:
- Filtered epoched data in MNE-Python format
- Visualization of the filter frequency response
- An HTML report comparing the original and filtered epochs (including their power spectral densities)

## Inputs

- **`epo`** (`neuro/meeg/mne/epochs`): epoched MEG/EEG data to filter (required)

## Outputs

- **`out_dir/meg-epo.fif`** (`neuro/meeg/mne/epochs`): filtered epoched data
- **`out_figs/filter_response.png`** (`generic/image/png`): frequency response plot of the applied filter
- **`out_report/report.html`** (`report/html`): HTML report comparing original and filtered epochs, with their power spectral densities

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `l_freq` | float \| null | `null` | For FIR filters, the lower pass-band edge; for IIR filters, the lower cutoff frequency. If `null`, the data are only low-passed. |
| `h_freq` | float \| null | `null` | For FIR filters, the upper pass-band edge; for IIR filters, the upper cutoff frequency. If `null`, the data are only high-passed. |
| `notch` | string | `""` | Comma-separated list of frequencies (Hz) to remove with a separate notch filter, e.g. `"50, 100, 150, 200"` for powerline noise and harmonics. Empty disables notch filtering. |
| `picks` | string | `""` | Channels to filter: channel type(s) (e.g. `"meg"`, `"eeg"`), channel names, indices, `"all"`, `"data"`, or empty for all data channels. |
| `filter_length` | string \| int | `"auto"` | Length of the FIR filter. `"auto"` chooses the length from the transition bandwidths; a string such as `"10s"` or `"5500ms"` gives a time duration; an int gives the length in samples. |
| `l_trans_bandwidth` | float \| string | `""` | Transition bandwidth at the low cut-off frequency (Hz). `"auto"` selects it automatically from `l_freq`. Only used for `method="fir"`. |
| `h_trans_bandwidth` | float \| string | `"auto"` | Transition bandwidth at the high cut-off frequency (Hz). `"auto"` selects it automatically from `h_freq`. Only used for `method="fir"`. |
| `method` | string | `"fir"` | Filter implementation: `"fir"` for overlap-add FIR filtering, or `"iir"` for forward-backward (`filtfilt`) IIR filtering. |
| `iir_params` | dict \| string | `""` | Parameters for IIR filtering (used only when `method="iir"`); see `mne.filter.construct_iir_filter()`. Empty/`null` uses a 4th-order Butterworth filter. |
| `phase` | string | `"zero"` | FIR filter phase, only used when `method="fir"`: `"zero"` (zero-phase, non-causal), `"zero-double"` (applied twice, non-causal), or `"minimum"` (minimum-phase, causal). |
| `fir_window` | string | `"hamming"` | Window function for FIR filter design: `"hamming"`, `"hann"`, or `"blackman"`. |
| `fir_design` | string | `"firwin"` | FIR design algorithm: `"firwin"` (`scipy.signal.firwin()`) or `"firwin2"` (`scipy.signal.firwin2()`). |
| `skip_by_annotation` | string \| list | `"('edge', 'bad_acq_skip')"` | Annotation prefixes marking segments that are filtered independently (e.g. epochs concatenated from recordings joined with `mne.concatenate_raws()`). Use an empty list to disable. |
| `pad` | string | `""` | Padding mode for FIR filters (only used when `method="fir"`); supports any `numpy.pad()` mode, plus `"reflect_limited"` (MNE's own default when unspecified). |

## Usage

### Running on Brainlife.io

1. Select your epoched MEG/EEG dataset as the `epo` input
2. Configure filtering parameters:
   - Set appropriate frequency bounds (`l_freq`, `h_freq`)
   - Optionally specify notch frequencies for powerline noise
   - Choose FIR or IIR method and adjust other parameters as needed
3. Submit the task
4. Monitor task completion and review the filter response plot and HTML report in the output viewer

### Local Testing

```bash
# Update config.json with your epoched data path
# Then run:
python main.py
```

## Technical Details

### Filter Implementation

- **FIR Filters**: Use overlap-add FFT-based filtering for efficiency. Zero-phase filtering is applied by default, which requires extra memory and computation but provides symmetric spectral characteristics.
- **IIR Filters**: Use forward-backward filtering (filtfilt) to achieve zero-phase response. Risk of filter instability with extreme parameters.

### Notch Filtering

When specified, notch filtering is applied as a separate step before bandpass filtering. Frequencies are parsed from comma-separated values and converted to integers.

### Report Generation

Uses MNE-Python's Report class to create an interactive HTML report with:
- Filter frequency response visualization
- Original epochs summary and power spectral density
- Filtered epochs summary and power spectral density

## Authors

- Maximilien Chaumon (https://github.com/dnacombo)

## Citations

- Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2
- Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded. We kindly ask that you acknowledge the funding below in your code and publications.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
