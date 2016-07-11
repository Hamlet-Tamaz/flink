(function() {
	angular
		.module('flink', ['ngMaterial'])
    .controller('homeCtr', home)
    .controller('dashCtr', dash)
		.controller('appCtrl', appCtrl)
    .controller('leftCtrl', leftNav)
		.controller('loginCtr', login)


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
    
    function signOut() {
      debugger
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        console.log('User signed out.');
      });

    }
  }

  function home() {
    var vm = this;
  }

  function login() {
    var vm = this;
    vm.name = 'hamlet'

    vm.onSignIn_google = function(googleUser) {
      vm.profile = googleUser.getBasicProfile();
      console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
      console.log('Name: ' + profile.getName());
      console.log('Image URL: ' + profile.getImageUrl());
      console.log('Email: ' + profile.getEmail());
      debugger
    }

    vm.signOut_google = function() {
      debugger
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        console.log('User signed out.');
      })
    }


    gapi.load('auth2', function() {
      gapi.auth2.init()
    })

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