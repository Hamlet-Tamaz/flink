(function() {
	angular
		.module('flink', ['ngMaterial'])
    .controller('dashCtr', dash)
		.controller('appCtrl', appCtrl)
		.controller('leftCtrl', leftNav)

		.config(function($mdThemingProvider) {
		  $mdThemingProvider.theme('dark-grey').backgroundPalette('grey').dark();
		  $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
		  $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
		  $mdThemingProvider.theme('dark-blue').backgroundPalette('blue').dark();
		})
		
		.config(function($mdThemingProvider) {
  			$mdThemingProvider.theme('default')
    			.primaryPalette('green')
          .accentPalette('pink');
    })
    // .config(function($interpolateProvider){
    //   $interpolateProvider.startSymbol('[[').endSymbol(']]');
    // });

	function dash() {
		var vm = this;

		vm.name ='Hamlet'


		vm.openLeftMenu = function() {
			$mdSidenav('left').toggle();
		};

    vm.openMenu = function($mdOpenMenu, ev) {
      originatorEv = ev;
      $mdOpenMenu(ev);
    };

		vm.friends = [{name: 'hamlet', age: 23}, {name: 'alain', age: 20}, {name: 'rufa', age: 41}]

	}





//  NOT MY STUFF

//  FOR SIDEBAR ON HOME PAGE

  function appCtrl ($scope, $timeout, $mdSidenav, $log) {
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    // $scope.isOpenRight = function(){
    //   return $mdSidenav('right').isOpen();
    // };
    /**
     * Supplies a function that will continue to operate until the
     * time is up.
     */
    function debounce(func, wait, context) {
      var timer;
      return function debounced() {
        var context = $scope,
            args = Array.prototype.slice.call(arguments);
        $timeout.cancel(timer);
        timer = $timeout(function() {
          timer = undefined;
          func.apply(context, args);
        }, wait || 10);
      };
    }
    /**
     * Build handler to open/close a SideNav; when animation finishes
     * report completion in console
     */
    function buildDelayedToggler(navID) {
      return debounce(function() {
        // Component lookup should always be available since we are not using `ng-if`
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }, 200);
    }
    function buildToggler(navID) {
      return function() {
        // Component lookup should always be available since we are not using `ng-if`
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }
    }
  }

  function leftNav($scope, $timeout, $mdSidenav, $log) {
    $scope.close = function () {
      // Component lookup should always be available since we are not using `ng-if`
      $mdSidenav('left').close()
        .then(function () {
          $log.debug("close LEFT is done");
        });
    };
  }



})()