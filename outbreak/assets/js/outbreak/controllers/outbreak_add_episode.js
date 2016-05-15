angular.module('opal.controllers').controller(
    'OutbreakAddEpisodeCtrl',
    function($modalInstance, $modal, options){
        modal = $modal.open({
  	    templateUrl: '/templates/modals/add_episode.html/',
  	    controller: 'AddEpisodeCtrl',
            size: 'lg',
  	    resolve: {
  		options: function() { return options; },
  		demographics: function() {
  		    return {}
  		},
                tags: function(){ return {} }
  	    }
  	}).result.then(function(result) {
  	    // The user has created the episode, or cancelled
  	    $modalInstance.close(result);
  	});

    }
)
