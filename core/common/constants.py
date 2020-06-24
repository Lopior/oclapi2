import re

HEAD = 'HEAD'
TEMP = '--TEMP--'

NAMESPACE_PATTERN = r'[a-zA-Z0-9\-\.\_]+'
NAMESPACE_REGEX = re.compile(r'^' + NAMESPACE_PATTERN + '$')

ACCESS_TYPE_VIEW = 'View'
ACCESS_TYPE_EDIT = 'Edit'
ACCESS_TYPE_NONE = 'None'
DEFAULT_ACCESS_TYPE = ACCESS_TYPE_VIEW
ACCESS_TYPE_CHOICES = ((ACCESS_TYPE_VIEW, 'View'),
                       (ACCESS_TYPE_EDIT, 'Edit'),
                       (ACCESS_TYPE_NONE, 'None'))
SUPER_ADMIN_USER_ID = 1
UPDATED_SINCE_PARAM = 'updatedSince'
RELEASED_PARAM = 'released'
PROCESSING_PARAM = 'processing'
ISO_639_1 = 'ISO 639-1'
