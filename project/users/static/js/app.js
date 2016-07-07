(function() {
	
angular
	.module('flink', ['ngMaterial'])
	.config(config)


function config($interpolateProvider) {
	$interpolateProvider.startSymbol('[[').endSymbol(']]')
}



})()