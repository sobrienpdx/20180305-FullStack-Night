var app = new Vue({
    el: '#app',
    data: {
        message: 'todos:',
        todos: [
            {'todo': 'Learn Vue.js', 'completed': false},
            {'todo': 'Master frontend', 'completed': false}
        ],
        todo: '',
    },
    methods: {
        addTodo: function() {
        },
        removeTodo: function(index) {
        },
        markDone: function(index) {
        },
    },
});
