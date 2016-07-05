(function() {
	
angular
	.module('flink', ['ngRoute', 'ngMaterial', 'ngMessages'])
	.config(config)


function config($routeProvider, $locationProvider, $interpolateProvider) {
	$interpolateProvider.startSymbol('[[').endSymbol(']]')

	// $routeProvider
	// 	.when('/flink', {
	// 		templateUrl: '../templates/home.html',
	// 		controller: 'homeCtrl',
	// 	})
}



})()