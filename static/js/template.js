// Sidebar close
const sidebarButton = document.querySelector(".close-sidebar");

function change () {
    var bigSidebar = document.querySelector(".sidebar-big");
    var smallSidebar = document.querySelector(".sidebar-small");
    bigSidebar.classList.toggle("is-hidden")
    smallSidebar.classList.toggle("is-hidden")
}

sidebarButton.addEventListener("click", change)

// Sidebar close
const sidebarButtonOpen = document.querySelector(".open-sidebar");

function change () {
    var bigSidebar = document.querySelector(".sidebar-big");
    var smallSidebar = document.querySelector(".sidebar-small");
    bigSidebar.classList.toggle("is-hidden")
    smallSidebar.classList.toggle("is-hidden")
}

sidebarButtonOpen.addEventListener("click", change)


// modal form projects creation

const modalProjectsFormButton = document.querySelector(".modalProjectsFormButton");
const modalProjectsFormCloser = document.querySelector(".modalProjectsFormCloser");
const modalProjectsFormCancel = document.querySelector(".modalProjectsFormCancel");
const modalBackground = document.querySelector(".modal-background")

function openModalProjectsForm () {
    var modalProjectsForm = document.querySelector(".modalProjectsForm");
    modalProjectsForm.classList.toggle("is-active")
}

function closeModalProjectsForm () {
    var modalProjectsForm = document.querySelector(".modalProjectsForm");
    modalProjectsForm.classList.toggle("is-active")
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModalProjectsForm($modal);
    });
  }

modalProjectsFormButton.addEventListener("click", openModalProjectsForm);
modalProjectsFormCloser.addEventListener("click", closeModalProjectsForm);
modalBackground.addEventListener("click", closeModalProjectsForm);
modalProjectsFormCancel.addEventListener("click", closeModalProjectsForm)

document.addEventListener('keydown', (event) => {
    if (event.code === 'Escape') {
        closeAllModals();
    }
  });


// success notification

var projectsForm = document.querySelector('.project-create-form');
var clientsForm = document.querySelector('.client-create-form');
var sucessmessage = document.querySelector('.successmessage');

function closeNotification () {
    var notification = document.querySelector(".notification");
    notification.classList.add("is-hidden");
}

function showNotification () {
    var notification = document.querySelector(".notification");
    notification.classList.remove("is-hidden");
    notification.classList.remove("is-primary");
    sucessmessage.classList.remove("is-hidden");
    setTimeout(closeNotification, 3000);
}

if(projectsForm.addEventListener){
    projectsForm.addEventListener("submit", showNotification());
}

if(clientsForm.addEventListener){
    clientsForm.addEventListener("submit", showNotification());
    console.log('worked');
}

