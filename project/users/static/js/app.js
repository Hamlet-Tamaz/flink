(function() {
	
angular
	.module('flink', ['ngMaterial'])
    .config(function($interpolateProvider){
      $interpolateProvider.startSymbol('[[').endSymbol(']]');
    });



})()