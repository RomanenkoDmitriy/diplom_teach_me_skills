
new Vue({
    el: '#comp_work',
    data: {
        orders: [],
        dat: []
    },
    created: function () {
        const vm = this;
        axios.get('/completed_work/api/')
            .then(function (response){
                console.log(response.data)
                vm.orders = response.data
                vm.dat = response.data.results
            })
    }
}
)