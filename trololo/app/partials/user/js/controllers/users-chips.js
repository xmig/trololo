angular.module('userApp').controller('userChipsCtrl', userChipsCtrl);

function userChipsCtrl ($timeout, $q, usersService, projectSelectedService, $scope) {
    var self = this;
    var pendingSearch, cancelSearch = angular.noop;
    var cachedQuery, lastSearch;
    self.allContacts = [];
    self.filterSelected = true;
    self.querySearch = querySearch;
    self.queryTaskSearch = queryTaskSearch;
    self.delayedQuerySearch = delayedQuerySearch;

    /**
     * Search for contacts; use a random delay to simulate a remote call
     */
    function querySearch (criteria) {
        usersService.get({ 'search': cachedQuery }, function (data) {
            self.allContacts = getFormatedUserData(data.results);
        });

        return cachedQuery ? self.allContacts.filter(createFilterFor(cachedQuery)) : [];
    }

    function queryTaskSearch (criteria) {
        projectSelectedService.get({ id: $scope.taskData.project }, function (data) {
            self.allContacts = data.members_data;

            var present = false;
            for (var i=0; i<self.allContacts.length; i++) {
                if (self.allContacts[i].id === data.owner.id) {
                    present = true;
                    break;
                }
            }

            if (!present) {
                self.allContacts.push(data.owner)
            }

            self.allContacts = getFormatedUserData(self.allContacts);
        });

        return cachedQuery ? self.allContacts.filter(createFilterFor(cachedQuery)) : [];
    }

    /**
     * Async search for contacts
     * Also debounce the queries; since the md-contact-chips does not support this
     */

    function delayedQuerySearch(criteria) {
      cachedQuery = criteria;
      if ( !pendingSearch || !debounceSearch() )  {
        cancelSearch();
        return pendingSearch = $q(function(resolve, reject) {
          // Simulate async search... (after debouncing)
          cancelSearch = reject;
          $timeout(function() {
            if ($scope.taskData != undefined) {
                resolve( self.queryTaskSearch(criteria) );
            } else {
                resolve( self.querySearch(criteria) );
            }
            refreshDebounce();
          }, 5, true)
        });
      }
      return pendingSearch;
    }

    function refreshDebounce() {
      lastSearch = 0;
      pendingSearch = null;
      cancelSearch = angular.noop;
    }

    /**
     * Debounce if querying faster than 300ms
     */
    function debounceSearch() {
      var now = new Date().getMilliseconds();
      lastSearch = lastSearch || now;
      return ((now - lastSearch) < 300);
    }

    /**
     * Create filter function for a query string
     */
    function createFilterFor(query) {
      var lowercaseQuery = angular.lowercase(query);
      return function filterFn(contact) {
        return (contact._lowerusername.indexOf(lowercaseQuery) != -1);;
      };
    }

//    function getFormatedUserData(users) {
//      return users.map(function (user, index) {
//        var contact = user;
//        console.log("contact:", contact);
//        contact._lowerusername = contact.username.toLowerCase();
//        return contact;
//      });
//    }

     function getFormatedUserData(users) {
      return users.map(function (user, index) {
        var contact = {
            username: user.username,
            email: user.email,
            photo: user.photo,
            id: user.id
        };
        contact._lowerusername = contact.username.toLowerCase();
        return contact;
      });
    }
}