angular.module('opal.controllers').controller(
    'OutbreakAddEpisodeCtrl',
    function($modalInstance, $modal, $route, options){
        modal = $modal.open({
  	    templateUrl: '/templates/modals/add_episode.html/',
  	    controller: 'AddEpisodeCtrl',
            size: 'lg',
  	    resolve: {
  		options: function() { return options; },
  		demographics: function() {
  		    return {}
  		},
                tags: function(){ return {tag: 'outbreak'} }
  	    }
  	}).result.then(function(result) {
  	    // The user has created the episode, or cancelled
            $route.reload();
            $modalInstance.close(result);
  	});

    }
)
