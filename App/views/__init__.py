# blue prints are imported 
# explicitly instead of using *
from .staff import staff_views
from .student import student_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin


views = [staff_views, index_views, auth_views, student_views] 
# blueprints must be added to this list