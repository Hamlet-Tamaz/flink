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
          .primaryPalette('green', {'default': 'A400'})
          .accentPalette('yellow', {'default': 'A400'})
          .warnPalette('pink');
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
    .controller('aboutusCtr', aboutus)
    .controller('homeCtr', home)
    .controller('dashCtr', dash)
		.controller('appCtr', appCtr)
    .controller('leftCtrl', leftCtr)
    .controller('loginCtr', login)
    .controller('calendarCtr', calendar)
		.controller('friendsCtr', friends)
    .controller('messagesCtr', messages)
    .controller('new_msgCtr', new_msg)


    setup.$inject = ['$http']
    function setup($http) {
      var vm = this;

      id = +location.pathname.split('/')[2]

      $http({
        method: "GET",
        url: `/api/users/${id}`,
        responseType: "json"
      }).then(function success(res) {
        vm.user = res.data



      }, function error(res) {
      vm.error = res

      })

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
        url: `/api/users/${id}`,
        responseType: "json"
      }).then(function success(res) {
        vm.user = res.data
        console.log('user: ', vm.user)


      }, function error(res) {
      vm.error = res

      })

      vm.states = ('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS ' +
      'MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI ' +
      'WY').split(' ').map(function(state) {
          return {abbrev: state};
        });



      vm.submitChanges = function(given_name, family_name, title, email, gender, picture, company, dob, address, address2, city, state, postalCode, biography) {

        vm.user.given_name = given_name
        vm.user.family_name = family_name
        vm.user.title = title
        vm.user.email = email
        vm.user.gender = gender
        vm.user.picture = picture
        vm.user.company = company
        vm.user.dob = dob
        vm.user.address = address
        vm.user.address2 = address2
        vm.user.city = city
        vm.user.state = state
        vm.user.postalCode = postalCode
        vm.user.biograph = biography


        $http({
          method: 'POST',
          url: `/api/users/${id}/edit`,
          data: vm.user,
          responseType: 'json'
        }).then(function success(res) {
          // id = res.data
          location.pathname = `/users/${id}/dash`

        }, function err(res) {

        })



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



    $http({
      method: "GET",
      url: `/api/users/${id}`,
      responseType: "json"
    }).then(function success(res) {
      vm.user = res.data
      vm.email = vm.user['email']

      $('#calendar').fullCalendar({

        googleCalendarApiKey: 'AIzaSyC3tsIjfaN2pbc6N82F7QKhccsqCCuZfrs',
        events: {
            googleCalendarId: vm.email
        }

      });
    }, function error(res) {
      vm.error = res

    })


    // $(document).ready(function() {
    //
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
      url: `/api/users/${id}`,
      responseType: "json"
    }).then(function success(res) {
      vm.user = res.data


      $http({
        method: "GET",
        url: `/api/users/${id}/friends/vis`,
        responseType: 'json'
      }).then(function success(res) {
        vm.friends_vis = res.data.items
        vm.tiles_vis = buildGridModel({}, vm.friends_vis);




        function buildGridModel(tileTmpl, friends){
          var it, results = [ ];
          for (var j=0; j<res.data.totalItems; j++) {

            it = angular.extend({},tileTmpl);

            it.img  = vm.friends_vis[j].image.url;
            it.title = vm.friends_vis[j].displayName;
            it.span  = { row : 1, col : 1 };
            it.google_id = vm.friends_vis[j].id

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


        $http({
          method: "GET",
          url: `/api/users/${id}/friends/con`,
          responseType: 'json'
        }).then(function success(res) {
          vm.friends_con = res.data.items
          vm.tiles_con = buildGridModel({}, vm.friends_con);




          function buildGridModel(tileTmpl, friends){
            var it, results = [ ];
            for (var j=0; j<res.data.totalItems; j++) {

              it = angular.extend({},tileTmpl);

              it.img  = vm.friends_vis[j].image.url;
              it.title = vm.friends_vis[j].displayName;
              it.span  = { row : 1, col : 1 };
              it.google_id = vm.friends_vis[j].id

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

        }, function error(res) {

        })

      }, function error(res) {

      })
    }, function error(res) {

    })




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
      url: `/api/users/${id}/messages/conversations`,
      responseType: 'json'
    }).then(function success(res) {

      vm.convos = res.data
      
    }, function error(res) {

    })

    $http({
      method: "GET",
      url: `/api/users/${id}`,
      responseType: 'json'
    }).then(function success(res) {
      vm.user = res.data

    }, function error(res) {

    })



    vm.getMessages = function (receiver_id) {
      vm.receiver_id = receiver_id

      // GETTING RECEIVER
      $http({
        method: "GET",
        url: `/api/users/${receiver_id}`,
        responseType: 'json'
      }).then(function success(res) {
        vm.receiverG = res.data
        // GETTING MESSAGES
        $http({
          method: "GET",
          url: `/api/users/${id}/messages/thread/${receiver_id}`,
          responseType: 'json'
        }).then(function success(res) {

          vm.inbox = res.data.inbox
          vm.outbox = res.data.outbox
          vm.user = res.data.user
          vm.receiver = res.data.receiver
          

          console.log('user: ', vm.user)
          console.log('receiver: ', vm.receiver)
          console.log('messages: ', vm.messages)

          debugger

        }, function error(res) {

        })

      }, function error(res) {

      })
    }




    // vm.test = [{title: 'title1', content: 'content1'},{title: 'title2', content: 'content2'}]



    vm.openLeftMenu = function() {
      $mdSidenav('left').toggle();
    }
  }





  function new_msg_W($http) {
    var vm = this;

    id = +location.pathname.split('/')[2]
    to_id = +location.pathname.split('/')[4]

    vm.weekdays = ['', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'];
    vm.selected = [0];
    vm.toggle = function (item, list) {
      var idx = list.indexOf(item);
      if (idx > -1) {
        list.splice(idx, 1);
      }
      else {
        list.push(item);
      }
    };
    vm.exists = function (item, list) {
      return list.indexOf(item) > -1;
    };
    vm.isIndeterminate = function() {
      return (vm.selected.length !== 0 &&
          vm.selected.length !== vm.items.length);
    };
    vm.isChecked = function() {
      return vm.selected.length === vm.items.length;
    };
    vm.toggleAll = function() {
      if (vm.selected.length === vm.items.length) {
        vm.selected = [];
      } else if (vm.selected.length === 0 || vm.selected.length > 0) {
        vm.selected = vm.items.slice(0);
      }
    };

    $http({
      method: "GET",
      url: `/api/users/${id}/friends/${to_id}`,
      responseType: 'json'
    }).then(function success(res) {

    }, function error(res) {

    })



  }


  function new_msg($http) {
    var vm = this;
    // vm.searchText = ''
    id = +location.pathname.split('/')[2]
    to_id = +location.pathname.split('/')[5]

    vm.sendFailed = false;

    //
    function createFilterFor(query) {
       var lowercaseQuery = angular.lowercase(query);
       return function filterFn(val) {
         return (val.displayName.search(vm.searchText) >= 0);
       };
     }

    vm.getMatches = function(data){
      return data.filter(createFilterFor(data))
    }


    vm.selectedItemChange = function(val){

      vm.receiverG = val
      vm.receiverG_id = val.id

      $http({
          method: "GET",
          url: `/api/users/${vm.receiverG_id}/google`,
          responseType: 'json'
        }).then(function success(res) {
          vm.receiver = res.data
          vm.message.receiver_id = vm.receiver.id

        }).catch(function error(res) {

        })
    }


    vm.stickers = [
       {name: 'Coffee', img_url: '/static/js/resources/pics/stickers/Coffee.png'},
       {name: 'Lunch', img_url: '/static/js/resources/pics/stickers/Lunch.png'},
       {name: 'Drinks', img_url: '/static/js/resources/pics/stickers/Drinks.png'},
       {name: 'Work', img_url: '/static/js/resources/pics/stickers/Work.png'}
     ]

    $http({
      method: "GET",
      url: `/api/users/${id}`,
      responseType: 'json'
    }).then(function success(res) {
        vm.user = res.data
        //
        // vm.img = '/static/js/resources/pics/stickers/Coffee.png'
        vm.message = {}
        vm.message.user_id = vm.user.id

        $http({
          method: "GET",
          url: `/api/users/${id}/friends/${to_id}`,
          responseType: 'json'
        }).then(function success(res) {
          vm.receiver = res.data
          //
        }).catch(function error(res) {
          //
        })
      })


    $http({
      method: "GET",
      url: `/api/users/${id}/friends/vis`,
      responseType: 'json'
    }).then(function success(res) {
      vm.friends = res.data

    })


     vm.sendMsg = function (occasion, content, date, dateRangeFrom, dateRangeUntil, weekdaysMon, weekdaysTues, weekdaysWed, weekdaysThurs, weekdaysFri, weekdaysSat, weekdaysSun, timeDesiredFrom, timeDesiredUntil) {
      debugger
      if (vm.receiver.id && occasion) {
        vm.message.occasion = occasion.trim()
        vm.message.content = content
        vm.message.date = date
        vm.message.dRangeFrom = dateRangeFrom
        vm.message.dateRangeUntil = dateRangeUntil
        vm.message.weekdaysMon = weekdaysMon
        vm.message.weekdaysTues = weekdaysTues
        vm.message.weekdaysWed = weekdaysWed
        vm.message.weekdaysThurs = weekdaysThurs
        vm.message.weekdaysFri = weekdaysFri
        vm.message.weekdaysSat = weekdaysSat
        vm.message.weekdaysSun = weekdaysSun
        vm.message.timeRangeFrom = timeDesiredFrom
        vm.message.timeRangeUntil = timeDesiredUntil


        $http({
          method: "POST",
          url: `/api/users/${id}/messages/new`,
          data: vm.message,
          responseType: 'json'
        }).then(function success(res) {


          location.pathname = `/users/${id}/dash`
        })
      }
      else {
        vm.sendFailed = true
      }
    }


  }

  
  function aboutus () {
    var vm = this


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