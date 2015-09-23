# These are settings for the FHIR class generator

from Python.mappings import *

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/DSTU2/'

# Whether and where to put the generated class models
write_resources = True
tpl_resource_target_ptrn = '../models/{}.py'            # where to write the generated class files to, with one placeholder for the class name

# Whether and where to put the factory methods
write_factory = True
tpl_factory_target = '../models/fhirelementfactory.py'

# Whether and where to write unit tests
write_unittests = True
tpl_unittest_target_ptrn = '../models/{}_tests.py'     # a pattern to determine the output files for unit tests; the one placeholder will be the class name


##
##  Know what you do when changing the following settings
##


# classes/resources
resource_modules_lowercase = True                       # whether all resource paths (i.e. modules) should be lowercase
tpl_resource_source = 'Python/template-resource.py'     # the template to use as source when writing resource implementations for profiles
resource_default_base = 'FHIRResource'                  # the default superclass to use for main profile models
contained_default_base = 'FHIRElement'                  # the default superclass to use for inline-defined (backbone) models
manual_profiles = [                                     # all these profiles should be copied to dirname(`tpl_resource_target_ptrn`): tuples of (path, module, profile-name-list)
    ('Python/fhirelement.py', 'fhirelement', [
        'boolean',
        'string', 'base64Binary', 'code', 'id',
        'decimal', 'integer', 'unsignedInt', 'positiveInt',
        'uri', 'oid', 'uuid',
        'Element',
    ]),
    ('Python/fhirresource.py', 'fhirresource', ['FHIRResource']),
    ('Python/fhircontainedresource.py', 'fhircontainedresource', ['ContainedResource']),
    ('Python/fhirreference.py', 'fhirreference', ['FHIRReference']),
    ('Python/fhirdate.py', 'fhirdate', ['date', 'dateTime', 'instant', 'time']),
    ('Python/fhirsearch.py', 'fhirsearch', ['FHIRSearch']),
]

# factory methods
tpl_factory_source = 'Python/template-elementfactory.py'

# search parameters
write_searchparams = False				# no longer implemented as of DSTU-2
search_generate_camelcase = False
tpl_searchparams_source = 'Python/template-searchparams.py'
tpl_searchparams_target = '../models/fhirsearchelement.py'

# unit tests
tpl_unittest_source = 'Python/template-unittest.py'
unittest_copyfiles = []
unittest_format_path_prepare = '{}'             # used to format `path` before appending another path element - one placeholder for `path`
unittest_format_path_key = '{}.{}'              # used to create property paths by appending `key` to the existing `path` - two placeholders
unittest_format_path_index = '{}[{}]'           # used for array properties - two placeholders, `path` and the array index
