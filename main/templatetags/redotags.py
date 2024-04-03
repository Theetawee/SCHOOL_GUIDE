from django import template

register = template.Library()


@register.filter
def redo_class(field, css_class):
    if css_class:
        field.field.widget.attrs["class"] = css_class

    return field


@register.filter
def redo_holder(field, placeholder):
    if placeholder:
        field.field.widget.attrs["placeholder"] = placeholder

    return field


@register.filter
def is_input(field):
    field.field.widget.attrs["class"] = (
        "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
    )
