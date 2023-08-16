#__init__.py
"""
This module analysis ambient seismic data using the Horizontal to Vertical Spectral Ratio (HVSR) technique
"""

from sprit.sprit import(
    run,
    check_mark,
    get_char,
    time_it,
    message,
    error,
    warning,
    info,
    checkifpath,
    input_params,
    gui,
    get_metadata,
    has_required_channels,
    fetch_data,
    batch_data_read,
    trim_data,
    generate_ppsds,
    process_hvsr,
    plot_stream,
    plot_specgram_stream,
    hvplot,
    plot_hvsr,
    plot_specgram_hvsr,
    select_windows,
    get_removed_windows,
    remove_noise,
    plot_noise_windows,
    check_peaks,
    get_report,
    HVSRData,
    HVSRBatch,
    test_class
)

__all__ =('sprit',
    'run',
    'check_mark',
    'get_char',
    'time_it',
    'message',
    'error',
    'warning',
    'info',
    'checkifpath',
    'input_params',
    'gui',
    'get_metadata',
    'has_required_channels',
    'fetch_data',
    'batch_data_read',
    'trim_data',
    'generate_ppsds',
    'process_hvsr',
    'plot_stream',
    'plot_specgram_stream',
    'hvplot',
    'plot_hvsr',
    'plot_specgram_hvsr',
    'select_windows',
    'get_removed_windows',
    'remove_noise',
    'plot_noise_windows',
    'check_peaks',
    'get_report',
    'HVSRData',
    'HVSRBatch',
    'test_class'
)

__author__ = 'Riley Balikian'