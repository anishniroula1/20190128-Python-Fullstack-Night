
const csrftoken = Cookies.get('csrftoken')
const headers = new Headers({
        "X-CSRFToken": csrftoken,
        'Accept': 'application/json',
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
            app.update()
    } catch (err) {
            console.log(err)
    }
}

const todo_list = window.location.pathname.split('/').pop()
const api_path = 'drf/api/'
const todo_lists_endpoint = 'todo_lists/' + todo_list
const todos_endpoint = 'todos/'
const api_root = `${window.location.protocol}//${window.location.host}/${api_path}`

const app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        todos: [],
        todo: '',
        editing: null,
        edit: null
    },
    mounted: function() {
        this.update()
    },
    methods: {
        update: async function() {
            try {
                const res = await fetch(api_root + todo_lists_endpoint)
                const json = await res.json()
                this.todos = json.todos
            } catch (err) {
                console.log(err)
            }
        },
            
        addTodo: function() {
            apiCall(api_root + todos_endpoint, 'POST', {
                text: this.todo,
                todo_list: todo_list
            })
            this.todo = ''
        },

        deleteTodo: function(todo) {
            apiCall(api_root + todos_endpoint + todo.id + '/', 'DELETE')
        },
            
        toggleTodo: function(todo) {
            apiCall(api_root + todos_endpoint + todo.id + '/', 'PATCH', {completed: !todo.completed})
        },        

        editTodo: function(todo) {
            apiCall(api_root + todos_endpoint + todo.id + '/', 'PATCH', {text: this.edit})
            this.editing = null
        },

        editView: function(todo) {
            this.editing = todo.id
            this.edit = todo.text
        }
    },
})