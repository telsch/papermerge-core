from .automate import AutomateSerializer
from .document import DocumentSerializer
from .document import DocumentDetailsSerializer
from .document_version import DocumentVersionSerializer
from .folder import FolderSerializer
from .node import NodeSerializer
from .node import NodeMoveSerializer
from .ocr import OcrSerializer
from .user import UserSerializer
from .group import GroupSerializer
from .tag import TagSerializer
from .role import RoleSerializer
from .password import PasswordSerializer
from .permission import PermissionSerializer
from .page import PageSerializer
from .content_type import ContentTypeSerializer
from .preferences import CustomUserPreferenceSerializer

__all__ = [
    'AutomateSerializer',
    'CustomUserPreferenceSerializer',
    'DocumentSerializer',
    'DocumentDetailsSerializer',
    'DocumentVersionSerializer',
    'FolderSerializer',
    'NodeSerializer',
    'NodeMoveSerializer',
    'OcrSerializer',
    'UserSerializer',
    'GroupSerializer',
    'TagSerializer',
    'RoleSerializer',
    'PasswordSerializer',
    'PermissionSerializer',
    'PageSerializer',
    'ContentTypeSerializer'
]
