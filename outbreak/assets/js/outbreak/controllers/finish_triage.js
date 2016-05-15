angular.module('opal.controllers').controller(
    'FinishTriageCtrl',
    function($scope, episode, options){
        $scope.episode = episode;
        $scope.options = options;
  	    for (var name in options) {
  		    if (name.indexOf('micro_test') != 0) {
  			    $scope[name + '_list'] = _.uniq(options[name]);
  		    };
  	    };
    }
)
