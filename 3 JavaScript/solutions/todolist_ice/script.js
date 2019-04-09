class TodoList {
  constructor() {
    this.todos = []
  }

  addTodo(task) {
    this.todos.push({task, completed: false})
  }

  toggleComplete(idx) {
    let todo = this.todos[idx]
    todo.completed = !todo.completed
    // // equivalent to above
    // if (todo.completed) {
    //   todo.completed = true
    // } else {
    //   todo.completed = false
    // }
  }

  deleteTodo(idx) {
    this.todos = this.todos.filter((todo, i) => i !== idx)
  }
}

// functions
const createTodoElement = (text) => {
  const elem = document.createElement('li')
  const deleteBtn = document.createElement('a')
  const toggleBtn = document.createElement('a')

  // create delete and toggle elements
  deleteBtn.innerHTML = '<i class="fas fa-times"></i>'
  deleteBtn.setAttribute('class', 'delete')
  toggleBtn.innerHTML = '<i class="fas fa-check"></i>'
  toggleBtn.setAttribute('class', 'toggle')

  // set elem with text
  elem.innerText = text

  // attach buttons to elem
  elem.appendChild(deleteBtn)
  elem.appendChild(toggleBtn)

  // btn event listeners
  deleteBtn.addEventListener('click', (evt) => {
    const li = evt.target.closest('li')
    const idx = parseInt(li.getAttribute('idx'))
    todoList.deleteTodo(idx)
    update(todoList)
  })

  toggleBtn.addEventListener('click', (evt) => {
    const li = evt.target.closest('li')
    const idx = li.getAttribute('idx')
    todoList.toggleComplete(idx)
    update(todoList)
  })  

  return elem
}

const update = (list) => {
    // clear all children from todosContainer
    while (todosContainer.lastChild) {
        todosContainer.removeChild(todosContainer.lastChild);
    }

    // map all todos to a new <li> element
    list.todos.map((todo, idx) => {
        const child = createTodoElement(todo.task)
        child.setAttribute('idx', idx)
        if (todo.completed) {
            child.classList.add('completed')
        } else {
            child.classList.remove('completed')
        }
        todosContainer.appendChild(child)
    }) 
}

// initialize todos
const todoList = new TodoList()

// selectors
const todoInput = document.querySelector('#todo-input')
const todosContainer = document.querySelector('#todos-container')

// event listeners
todoInput.addEventListener('keydown', (evt) => {
  if (evt.key === 'Enter') {
    todoList.addTodo(todoInput.value)
    // todoList.addTodo(evt.target.value) // equivalent
    update(todoList)
    todoInput.value = ''
  }
})