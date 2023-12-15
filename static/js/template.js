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




