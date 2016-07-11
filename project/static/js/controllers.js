(function() {
	angular 
		.module('flink', ['ngMaterial'])
		.controller('baseCtr', base)


	function base() {
		var vm = this;
		vm.openMenu = function($mdOpenMenu, ev) {
      		originatorEv = ev;
      		$mdOpenMenu(ev);
    	};

	}
})()