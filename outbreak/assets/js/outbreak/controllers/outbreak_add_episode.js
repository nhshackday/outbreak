angular.module('opal.controllers').controller(
    'OutbreakAddEpisodeCtrl',
    function($scope, $modalInstance, $modal, $route, $q, Episode, UserProfile){
        modal = $modal.open({
  	    templateUrl: '/templates/modals/add_episode.html/',
  	    controller: 'AddEpisodeCtrl',
            size: 'lg',
  	    resolve: {
                referencedata: function(Referencedata) { return Referencedata; },
  		demographics: function() {
  		    return {}
  		},
                tags: function(){ return {tag: 'outbreak'} }
  	    }
  	}).result.then(function(result) {
  	    // The user has created the episode, or cancelled

            if(result){
                $scope.episode = new Episode(result);
                var deferred = $q.defer();
                $modalInstance.close(deferred.promise);

                var item = $scope.episode.newItem('presenting_symptoms');
                $scope.episode.presenting_symptoms[0] = item;
                modal = $modal.open({
                    templateUrl: '/templates/modals/presenting_symptoms.html/',
                    controller: 'EditItemCtrl',
                    size: 'lg',
                    resolve: {
                        item: function() { return item; },
                        referencedata: function(Referencedata) { return Referencedata; },
                        metadata: function(Metadata) { return Metadata; },
                        episode: function() { return $scope.episode; },
                        profile: function(UserProfile) { return UserProfile }
                    }
                }).result.then(
                    function(){deferred.resolve($scope.episode);
                               $route.reload();},
                    function(){deferred.resolve($scope.episode)}
                );
            }else{
                $modalInstance.close(result);
            }


            // $modalInstance.close(result);
  	});

        $scope.cancel = function() {
	    $modalInstance.close('cancel');
        };


    }
)
