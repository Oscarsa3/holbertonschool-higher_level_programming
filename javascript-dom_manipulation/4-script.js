const addItem = document.getElementById("add_item");
addItem.addEventListener("click", function () {
    const mylist = document.querySelector(".my_list");
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    mylist.appendChild(newItem); 
})