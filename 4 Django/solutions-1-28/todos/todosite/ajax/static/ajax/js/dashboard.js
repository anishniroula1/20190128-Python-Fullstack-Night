// dashboard.js
// ajax example with custom made api

const csrftoken = Cookies.get('csrftoken')
const headers = new Headers({
    "X-CSRFToken": csrftoken
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

async function update() {
    const res = await fetch('api/todo_lists/')
    const json = await res.json()

    const lists = JSON.parse(json)

    while (todos_container.lastChild) {
        todos_container.removeChild(todos_container.lastChild);
    }

    for (let list of lists) {
        const todo_list = document.createElement('li')
        const link = document.createElement('a')
        const deleteBtn = document.createElement('i')
        
        link.innerText = list.fields.title
        link.setAttribute('href', 'todo_list/'+list.pk)

        deleteBtn.classList.add('fa', 'fa-times')
        deleteBtn.addEventListener('click', function() {
            apiCall('api/todo_list/'+list.pk, 'DELETE')
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
    apiCall('api/todo_lists/', 'POST', {todo_list: todo_list_input.value})
})