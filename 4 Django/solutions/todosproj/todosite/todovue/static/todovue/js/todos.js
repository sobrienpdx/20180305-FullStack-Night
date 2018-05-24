var app = new Vue({
    el: '#app',
    delimiters: ['${','}'],
    http: {
        root: 'http://localhost:8000/todovue/api/',
        headers: {
            Authorization: 'Token dd0f5ce82fc39789953aaa0e250bc8f955b7248f',
            csrftoken: Cookies.get('csrftoken'),
        },
    },
    data: {
        message: 'todos:',
        todos: [],
        todo: '',
        loading: true,
    },
    methods: {
        getTodos: function() {
            this.loading = true;
            this.$http.get('todos/')
                .then((response) => {
                    this.todos = response.body;
                    this.loading = false;
                })
                .catch((err) => {
                    console.log(err);
                    this.loading = false;
                });
        },
        addTodo: function() {
            this.loading = true;
            this.$http.post('todos/', {'text': this.todo})
                .then((response) => {
                    this.getTodos();
                    this.loading = false;
                    this.todo = '';
                })
                .catch((err) => {
                    console.log(err);
                    this.loading = false;
                });
        },
        removeTodo: function(pk) {
            this.loading = true;
            this.$http.delete(`todos/${pk}/`)
                .then((response) => {
                    this.getTodos();
                    this.loading = false;
                })
                .catch((err) => {
                    console.log(err);
                    this.loading = false;
                });
        },
        markDone: function(pk, completed) {
            this.loading = true;
            this.$http.patch(`todos/${pk}/`, {'completed': !completed})
                .then((response) => {
                    this.getTodos();
                    this.loading = false;
                })
                .catch((err) => {
                    console.log(err);
                    this.loading = false;
                });
        },
    },
    computed: {

    },
    mounted: function() {
        this.getTodos();
    }
});
