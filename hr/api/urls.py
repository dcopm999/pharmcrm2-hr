from rest_framework import routers

from hr.api import views

router = routers.SimpleRouter()
router.register("category", views.CategoryViewSet)
router.register("department", views.DepartmentViewSet)
router.register("specialization", views.SpecializationViewSet)
router.register("position", views.PositionViewSet)
router.register("staff", views.StaffViewSet)
router.register("contact", views.ContactViewSet)
router.register("education", views.EducationViewSet)
router.register("experience", views.ExperienceViewSet)
router.register("persinalrow", views.PersonalRowViewSet)

urlpatterns = router.urls
