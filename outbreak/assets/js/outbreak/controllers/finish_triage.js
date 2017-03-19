angular.module('opal.controllers').controller(
    'FinishTriageCtrl',
    function($scope, $modalInstance, episode, referencedata){
        $scope.status = {
            saved : false
        }
        $scope.episode = episode;
        _.extend($scope, referencedata.toLookuplists());

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
