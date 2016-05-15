angular.module('opal.controllers').controller(
    'FinishTriageCtrl',
    function($scope, $modalInstance, episode, options){
        $scope.status = {
            saved : false
        }
        $scope.episode = episode;
        $scope.options = options;
  	    for (var name in options) {
  		    if (name.indexOf('micro_test') != 0) {
  			    $scope[name + '_list'] = _.uniq(options[name]);
  		    };
  	    };

        $scope.save = function() {
	    $scope.status.saved = true;
        };

        $scope.cancel = function() {
	        $modalInstance.close('cancel');
        };

        $scope.admit = function(){
            var tagging = $scope.episode.getItem('tagging', 0)
                tagging.save({}).then(
                    function(){
                        $modalInstance.close('discharged')
                    }
                )

        };

        $scope.discharge = function(){
            $scope.admit();
        }

    }
)
