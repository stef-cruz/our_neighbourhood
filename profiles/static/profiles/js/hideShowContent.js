// Constants
const myDetailsButton = document.getElementById("js-my-details-button")
const myDetailsContent = document.getElementById("js-my-details-content")
const myPostsButton = document.getElementById("js-my-posts-button")
const myPostsContent = document.getElementById("js-my-posts-content")

//Event listener to display content when button is clicked
myDetailsButton.addEventListener("click", () => {
    myDetailsContent.style.display = 'block';
    myPostsContent.style.display = 'none';
    myDetailsButton.classList.add('active');
    myPostsButton.classList.remove('active');
});

myPostsButton.addEventListener("click", () => {
    myDetailsContent.style.display = 'none';
    myPostsContent.style.display = 'block';
    myPostsButton.classList.add('active');
    myDetailsButton.classList.remove('active');
});
