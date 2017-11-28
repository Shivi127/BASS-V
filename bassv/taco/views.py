from django.shortcuts import render
from .models import *
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseReviewCreateForm


def courseupdate_createview(request):
    template_name='courses/(?P<pk>\\d+)/updates/create/'
    context={}
    return render (request, template_name, context)
# Create your views here.
@login_required
def index(request):
    """
    View function for home page of site.
    """
    # # Generate counts of some of the main objects
    # class_iter = Course.objects.all()
    # num_instances = BookInstance.objects.all().count()
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    cr=Course.objects.filter(ta={Ta.full_name})
    context = dict()
    # for item in class_iter:
    #     context[str(item)] = item.cname

    return render(
        request,
        'index.html',
    #     context={'num_books': num_books, 'num_instances': num_instances,
    #              'num_instances_available': num_instances_available, 'num_authors': num_authors},
        context,
    )

class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course

class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Course


class CourseReviewListView(LoginRequiredMixin, generic.ListView):
    model = CourseReview

def coursereview_createview(request, pk):

    def _init_(self,*args,**kwargs):
        self.user = kwargs.pop('user')
  # course = get_object_or_404(Course, pk)

  form = CourseReviewCreateForm(request.POST,user=request.user)
  # errors = None


  if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('course_detail', kwargs=(course.cid)))

  if form.errors
      print(form.errors)

  template_name= 'taco/form.html'
  context={"form":form}
  return render(request, template_name, context)
  #


class CourseReviewCreateView(CreateView):
    form_class=CourseReviewCreateForm
    template_name='/taco/form.html'