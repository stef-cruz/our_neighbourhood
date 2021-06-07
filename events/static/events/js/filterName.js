/*
Filter text to change according to filter that the user selects
*/

// Selector
const filterValue = document.getElementById('filter-value-js');

// Get search parameter in the URL and change filter text
if (window.location.search === '?category=arts') {
    filterValue.innerText = 'Arts';
} else if (window.location.search === '?category=food-and-drinks'){
    filterValue.innerText = 'Food & Drinks';
} else if (window.location.search === '?category=fitness-and-sports'){
    filterValue.innerText = 'Fitness & Sports';
} else if (window.location.search === '?category=kids'){
    filterValue.innerText = 'Kids';
} else if (window.location.search === '?category=services'){
    filterValue.innerText = 'Services';
} else if (window.location.search === '?category=other'){
    filterValue.innerText = 'Other';
} else if (window.location.search === '?date=upcoming-events'){
    filterValue.innerText = 'Upcoming Events';
}

