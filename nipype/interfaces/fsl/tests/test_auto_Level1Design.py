# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.model import Level1Design

def test_Level1Design_inputs():
    input_map = dict(bases=dict(mandatory=True,
    ),
    contrasts=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    interscan_interval=dict(mandatory=True,
    ),
    model_serial_correlations=dict(mandatory=True,
    ),
    session_info=dict(mandatory=True,
    ),
    )
    inputs = Level1Design.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Level1Design_outputs():
    output_map = dict(ev_files=dict(),
    fsf_files=dict(),
    )
    outputs = Level1Design.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

