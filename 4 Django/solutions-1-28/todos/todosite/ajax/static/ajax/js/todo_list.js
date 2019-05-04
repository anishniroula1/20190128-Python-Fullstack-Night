
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
            app.update()
    } catch (err) {
            console.log(err)
    }
}

const todo_list = window.location.pathname.split('/').pop()
const api_path = 'ajax_todos/api/todo_list/' + todo_list
const api_root = `${window.location.protocol}//${window.location.host}/${api_path}/`

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
                const res = await fetch(api_root)
                const json = await res.json()
                this.todos = JSON.parse(json.todos)
            } catch (err) {
                console.log(err)
            }
        },
            
        addTodo: function() {
            apiCall(api_root, 'POST', {todo: this.todo})
        },

        deleteTodo: function(pk) {
            apiCall(api_root+pk, 'DELETE')
        },
            
        toggleTodo: function(pk) {
            apiCall(api_root+pk, 'PUT', {toggle: true})
        },        

        editTodo: function(pk) {
            apiCall(api_root+pk, 'PUT', {todo: this.edit})
            this.editing = null
        },

        editView: function(pk) {
            this.editing = pk
            const todo = this.todos.find(elem => elem.pk === pk)
            this.edit = todo.fields.text
        }
    },
})