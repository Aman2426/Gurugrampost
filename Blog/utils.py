from django.shortcuts import render, redirect, get_object_or_404

class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        print(request.POST)
        print(request.FILES)
        bound_form = self.form_class(request.POST,request.FILES)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})
        
class ObjectUpdateMixin:
    form_class=None
    template_name=''
    model=None

    def get(self, request, pk):  
        obj = get_object_or_404(self.model,pk=pk)
        context={'form':self.form_class(instance=obj)}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = get_object_or_404(self.model,pk=pk)
        bound_form= self.form_class(request.POST, request.FILES, instance=obj)
        if bound_form.is_valid():
            new_obj= bound_form.save()
            return redirect(new_obj)
        else: 
            context={'form':bound_form,'obj':obj}
            return render(request, self.template_name, context)
