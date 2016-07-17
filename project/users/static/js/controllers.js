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
      $mdIconProvider
      .iconSet("avatar", 'icons/avatar-icons.svg', 128)
      .iconSet("call", 'img/icons/sets/communication-icons.svg', 24)
      .iconSet("social", 'img/icons/sets/social-icons.svg', 24)

    })
    .config(function($interpolateProvider){
      $interpolateProvider.startSymbol('[[').endSymbol(']]');
    })


    .controller('setupCtr', setup)
    .controller('editCtr', edit)
    .controller('homeCtr', home)
    .controller('dashCtr', dash)
		.controller('appCtr', appCtr)
    .controller('leftCtrl', leftCtr)
    .controller('loginCtr', login)
    .controller('calendarCtr', calendar)
		.controller('friendsCtr', friends)
    .controller('messagesCtr', messages)

    
    setup.$inject = ['$http']
    function setup($http) {
      var vm = this;
      
      id = +location.pathname.split('/')[2]

      $http({
        method: "GET",
        url: `http://localhost:3000/api/users/${id}`,
        responseType: "json"
      }).then(function success(res) {
        vm.user = res.data

        debugger
      
      }), function error(res) {
      vm.error = res
      debugger
      }

      // vm.user = {
      //   title: 'Developer',
      //   email: 'ipsum@lorem.com',
      //   firstName: '',
      //   lastName: '',
      //   company: 'Google',
      //   address: '1600 Amphitheatre Pkwy',
      //   city: 'Mountain View',
      //   state: 'CA',
      //   biography: 'Loves kittens, snowboarding, and can type at 130 WPM.\n\nAnd rumor has it she bouldered up Castle Craig!',
      //   postalCode: '94043'
      // };

      vm.states = ('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS ' +
      'MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI ' +
      'WY').split(' ').map(function(state) {
          return {abbrev: state};
        });
    }

    edit.$inject = ['$http']
    function edit($http) {
      var vm = this;
      
      id = +location.pathname.split('/')[2]

      $http({
        method: "GET",
        url: `http://localhost:3000/api/users/${id}`,
        responseType: "json"
      }).then(function success(res) {
        vm.user = res.data
        console.log('user: ', vm.user)
        debugger
      
      }), function error(res) {
      vm.error = res
      debugger
      }
      
      vm.states = ('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS ' +
      'MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI ' +
      'WY').split(' ').map(function(state) {
          return {abbrev: state};
        });
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

      
      $http({
        method: "GET",
        url: `http://localhost:3000/api/users/${id}/friends`,
        responseType: 'json'
      }).then(function success(res) {
        vm.friends = res.data.items
debugger
        vm.tiles = buildGridModel({});


        function buildGridModel(tileTmpl){
          var it, results = [ ];
          for (var j=0; j<res.data.totalItems; j++) {

            it = angular.extend({},tileTmpl);

            it.img  = vm.friends[j].image.url;
            it.title = vm.friends[j].displayName;
            it.span  = { row : 1, col : 1 };
            it.google_id = vm.friends[j].id

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


    var originatorEv;
    vm.menuHref = "http://www.google.com/design/spec/components/menus.html#menus-specs";
    vm.openMenu = function($mdOpenMenu, ev) {
      originatorEv = ev;
      $mdOpenMenu(ev);
    };
    // vm.announceClick = function(index) {
    //   $mdDialog.show(
    //     $mdDialog.alert()
    //       .title('You clicked!')
    //       .textContent('You clicked the menu item at index ' + index)
    //       .ok('Nice')
    //       .targetEvent(originatorEv)
    //   );
    //   originatorEv = null;
    // };

  }



  messages.$inject = ['$http', '$mdSidenav']
  function messages ($http, $mdSidenav) {
    var vm = this;
    
    id = +location.pathname.split('/')[2]
    
    $http({
      method: "GET",
      url: `http://localhost:3000/api/users/${id}/messages/conversations`,
      responseType: 'json'
    }).then(function success(res) {
      vm.conversations = res.data
      debugger
      
    }), function error(res) {
      debugger
    }
    
    debugger
    vm.inbox = [{title: 'title1', content: 'content1'},{title: 'title2', content: 'content2'}]

    

    vm.openLeftMenu = function() {
      $mdSidenav('left').toggle();
    }
  }
  




  function new_message($http) {
    var vm = this;

    id = +location.pathname.split('/')[2]
    to_id = +location.pathname.split('/')[4]

    $http({
      method: "GET",
      url: `http://localhost:3000/api/users/${id}/friends/${to_id}`,
      responseType: 'json'
    }).then(function success(res) {
      debugger
    }), function error(res) {

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