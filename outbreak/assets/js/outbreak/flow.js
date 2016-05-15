//
// Service for defining flow
//
angular.module('opal.services').factory('OutbreakFlow', function(){
    var Flow = {
        enter: function(){
            return {
                'controller': 'OutbreakAddEpisodeCtrl',
                'template': '/templates/modals/add_episode.html/'
            }
        },
        exit: function(){
            return  {
                'controller': 'FinishTriageCtrl',
                'template'  : '/templates/finish_triage.html'
            }
        }

    };
    return Flow;
})
