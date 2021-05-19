from django import template
# Source: https://origin.tiltingatwindmills.dev/how-to-show-a-range-of-page-numbers-using-djangos-pagination

register = template.Library()


@register.filter
def page_window(page, last, size=7):
    if page < size // 2 + 1:
        return range(1, min(size+1, last + 1))

    else:
        return range(page - size // 2, min(last + 1, page + 1 + size // 2))