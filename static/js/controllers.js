(function() {
	angular
		.module('flink')
		.controller('homeCtr', home)
		.controller('baseCtr', base)

		function home() {
			var vm = this;

			vm.name = 'hamlet'

			vm.currentNavItem = 'page1'
		}

		function base() {
			var vm = this;

			vm.name ='Hamlet'

			vm.currentNavItem = 'page1'

			vm.openLeftMenu = function() {
				$mdSidenav('left').toggle();
			};

		}
})()