# blue prints are imported 
# explicitly instead of using *
from .index import index_views
from .auth import auth_views
from .shelters import shelter_views
from .donations import donation_views
from .faq import faq_views


views = [index_views, auth_views,shelter_views,donation_views,faq_views] 
# blueprints must be added to this list