// dashboard.js
// ajax example with custom made api

const csrftoken = Cookies.get('csrftoken')
const headers = new Headers({
    "X-CSRFToken": csrftoken,
    'Content-Type': 'application/json'    
});

async function apiCall(url, request_type, body) {
    const options = {
        method: request_type,
        credentials: 'same-origin',
        headers: headers,
        body: JSON.stringify(body)
    }
    try {
        const res = await fetch(url, options)
        update()
    } catch (err) {
        console.log(err)
    }
}

// selectors
const todo_list_input = document.querySelector('#todo-list-input')
const submit_btn = document.querySelector('#todo-list-submit')
const todo_list_delete = document.querySelectorAll('.delete')
const todos_container = document.querySelector('#todos-container')
const api_root = 'http://localhost:8000/drf/api/'


async function update() {
    const res = await fetch(api_root + 'todo_lists/')
    const lists = await res.json()
    console.log(lists)

    while (todos_container.lastChild) {
        todos_container.removeChild(todos_container.lastChild);
    }

    for (let list of lists) {
        const todo_list = document.createElement('li')
        const link = document.createElement('a')
        const deleteBtn = document.createElement('i')
        
        link.innerText = list.title
        link.setAttribute('href', 'list/'+list.id)

        deleteBtn.classList.add('fa', 'fa-times')
        deleteBtn.addEventListener('click', function() {
            apiCall(api_root + 'todo_lists/'+list.id, 'DELETE')
        })

        todo_list.appendChild(link)
        todo_list.appendChild(deleteBtn)
        todos_container.appendChild(todo_list)
    }
}

// event listeners & ajax
window.addEventListener('load', function() {
    update()
})


submit_btn.addEventListener('click', function(evt){
    apiCall(api_root + 'todo_lists/', 'POST', {title: todo_list_input.value})
})