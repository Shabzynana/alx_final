# todoapp
The Todo App is an advanced web-based application that allows users to manage their daily tasks and keep track of their progress. With this application, users can easily create, update, and delete tasks, set due dates and prioritize their to-do list.

{% url 'register' %}

{% extends "user/base.html" %}
{% block content %}


<form method="POST" enctype="multipart/form-data">
    <!-- Security token -->
    {% csrf_token %}

    <!-- Using the formset -->
    {{ form }}

    <input type="submit" value="Submit">


</form>

{% endblock content %}



<!-- {% extends "user/base.html" %}
{% block content %}
<div class="main">
  <div class="jumbotron">
    {{ object.title }}<br/>
    {{ object.content }}<br/>

    {{ object.date_created|date:"F d, Y" }}<br/>
  <a href="{% url 'task_update' task.id %}">
    <button class="border-0 btn-transition btn btn-outline-success">
      <i class="fa fa-edit">
      </i>
    </button>
  </a>
  <a href="{% url 'task_delete' task.id %}">
    <button type="button" class="border-0 btn-transition btn btn-outline-danger" data-toggle="modal" data-target="#exampleModalLong">
      <i class="fa fa-trash">
      </i>
    </button>
  </a>

  </div>
</div>

{% endblock content %} -->






{% for task in page_task %}
<div class="jumbotroon">
  <article class="media content-section">
    <div class="media-body">
      <div class="article-metadata">
        <p class="mr-2">Id: {{ task.id }}</p>
      </div>
      <h6><a class="article-title" href="{% url 'task_detail' task.id %}">Title: {{ task.title }}</a></h6>
      <p class="article-content">Task: {{ task.content }}</p>
      <p class="article-content">Start_Date: {{ task.start_date|date:"F d, Y" }}</p>
      <p class="article-content">End_Date: {{ task.end_date|date:"F d, Y" }}</p>
    </div>
  </article>
</div>
{% endfor %}

{% if page_task.has_previous %}
  <a class="btn btn-outline-primary" href="?page={{ page_task.previous_page_number }}">Previous</a>
{% endif %}

{% for num in page_task.paginator.page_range %}

  {% if num %}

    {% if page_task.number == num %}
      <a class="btn btn-primary" href="?page={{ num }}">{{ num }}</a>
    {% else %}
      <a class="btn btn-outline-primary" href="?page={{ num }}">{{ num }}</a>
    {% endif %}

  {% else %}
   ...
  {% endif %}



{% if page_task.has_next %}
  <a class="btn btn-outline-primary" href="?page={{ page_task.next_page_number }}">Next</a>
{% endif %}
