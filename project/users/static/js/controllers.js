// Move out All API KEYS!!!

(function() {
	angular
		.module('flink', ['ngMaterial'])


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
    .config(function( $mdIconProvider ){
      $mdIconProvider.iconSet("avatar", 'icons/avatar-icons.svg', 128);
    })
    .config(function($interpolateProvider){
      $interpolateProvider.startSymbol('[[').endSymbol(']]');
    })



    .controller('homeCtr', home)
    .controller('dashCtr', dash)
		.controller('appCtr', appCtr)
    .controller('leftCtrl', leftCtr)
    .controller('loginCtr', login)
    .controller('calendarCtr', calendar)
		.controller('friendsCtr', friends)
    .controller('messagesCtr', messages)

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
    }

    vm.signOut_google = function() {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        console.log('User signed out.');
      })
    }
  }



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

  calendar.$inject = ['$http']
  function calendar($http) {
    var vm = this;
    

    id = +location.pathname.split('/')[2]

debugger

    $http({
      method: "GET",
      url: `http://localhost:3000/api/users/${id}`,
      responseType: "json"
    }).then(function success(res) {
      vm.user = res.data
      vm.email = vm.user['email']
      debugger
      $('#calendar').fullCalendar({

        googleCalendarApiKey: 'AIzaSyC3tsIjfaN2pbc6N82F7QKhccsqCCuZfrs',
        events: {
            googleCalendarId: vm.email
        }

      });
    }), function error(res) {
      vm.error = res
      debugger
    }


    // $(document).ready(function() {
    // debugger
    //   $('#calendar').fullCalendar({

    //     googleCalendarApiKey: 'AIzaSyC3tsIjfaN2pbc6N82F7QKhccsqCCuZfrs',
    //     events: {
    //         googleCalendarId: vm.user['email']
    //     }

    //   });
    // });
  }


  friends.$inject = ['$http']
  function friends($http) {
    var vm = this;
    
    id = +location.pathname.split('/')[2]

    $http({
      method: "GET",
      url: `http://localhost:3000/api/users/${id}`,
      responseType: "json"
    }).then(function success(res) {
      vm.user = res.data
      debugger
      
      $http({
        method: "GET",
        url: `http://localhost:3000/api/users/${id}/friends`,
        responseType: 'json'
      }).then(function success(res) {
        vm.friends = res.data.items
        
        vm.tiles = buildGridModel({
                icon : "avatar:svg-",
                title: "Svg-",
                background: ""
              });
        debugger 

        function buildGridModel(tileTmpl){
          var it, results = [ ];
          for (var j=0; j<11; j++) {
            it = angular.extend({},tileTmpl);
            it.icon  = it.icon + (j+1);
            it.title = it.title + (j+1);
            it.span  = { row : 1, col : 1 };
            switch(j+1) {
              case 1:
                it.background = "red";
                it.span.row = it.span.col = 2;
                break;
              case 2: it.background = "green";         break;
              case 3: it.background = "darkBlue";      break;
              case 4:
                it.background = "blue";
                it.span.col = 2;
                break;
              case 5:
                it.background = "yellow";
                it.span.row = it.span.col = 2;
                break;
              case 6: it.background = "pink";          break;
              case 7: it.background = "darkBlue";      break;
              case 8: it.background = "purple";        break;
              case 9: it.background = "deepBlue";      break;
              case 10: it.background = "lightPurple";  break;
              case 11: it.background = "yellow";       break;
            }
            results.push(it);
          }

          return results;
        }

      }), function error(res) {
        debugger
      }

    }), function error(res) {
      debugger
    }
  }




  function messages ($mdSidenav) {
    var vm = this;

    vm.inbox = [{title: 'title1', content: 'content1'},{title: 'title2', content: 'content2'}]

    vm.openLeftMenu = function() {
      $mdSidenav('left').toggle();
    }
  }
  
    // gapi.load('auth2', function() {
    //   gapi.auth2.init()
    // })





//  NOT MY STUFF

//  FOR SIDEBAR ON HOME PAGE
  // appCtr.$inject = ['$mdSidenav', '$timeout', '$log']
  function appCtr ($mdSidenav, $timeout, $log) {

    var vm = this;

    vm.toggleLeft = buildDelayedToggler('left');
    vm.toggleRight = buildToggler('right');
    // vm.isOpenRight = function(){
    //   return $mdSidenav('right').isOpen();
    // };
    /**
     * Supplies a function that will continue to operate until the
     * time is up.
     */
    function debounce(func, wait, context) {
      var timer;
      return function debounced() {
        var context = vm,
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

  function leftCtr($timeout, $mdSidenav, $log) {
    var vm = this;

    vm.close = function () {
      // Component lookup should always be available since we are not using `ng-if`
      $mdSidenav('left').close()
        .then(function () {
          $log.debug("close LEFT is done");
        });
    };
  }



})()