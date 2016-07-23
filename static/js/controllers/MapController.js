app.controller('MapController', ['$scope','$http','uiGmapLogger','uiGmapGoogleMapApi', function ($scope,$http,$log,GoogleMapApi) {

    //Check if browser has geo activated
    $scope.geolocationAvailable = navigator.geolocation ? true : false;

    var style = [{"featureType":"landscape","stylers":[{"hue":"#FFBB00"},{"saturation":43.400000000000006},{"lightness":37.599999999999994},{"gamma":1}]},{"featureType":"road.highway","stylers":[{"hue":"#FFC200"},{"saturation":-61.8},{"lightness":45.599999999999994},{"gamma":1}]},{"featureType":"road.arterial","stylers":[{"hue":"#FF0300"},{"saturation":-100},{"lightness":51.19999999999999},{"gamma":1}]},{"featureType":"road.local","stylers":[{"hue":"#FF0300"},{"saturation":-100},{"lightness":52},{"gamma":1}]},{"featureType":"water","stylers":[{"hue":"#0078FF"},{"saturation":-13.200000000000003},{"lightness":2.4000000000000057},{"gamma":1}]},{"featureType":"poi","stylers":[{"hue":"#00FF6A"},{"saturation":-1.0989010989011234},{"lightness":11.200000000000017},{"gamma":1}]}];

    //Map initial config
    $scope.map = {
        center: {
            latitude: 40.7829,
            longitude: 73.9654
        },
        zoom: 15,
        options: {
            streetViewControl: false,
            mapTypeControl: false,
            scaleControl: true,
            rotateControl: false,
            zoomControl: true,
            draggable: true,
            disableDefaultUI: true,
            clickableIcons: false,
            styles: style
        }
    };

    $scope.GetMarkers = function () {

    //Will get markers with actual scope coord values
        var httpRequest = $http({
            method: 'GET',
            dataType:'json',
            url: '/api/'+$scope.map.center.latitude+'/'+$scope.map.center.longitude

        }).success(function (data) {
            $scope.pokemonMarkers = (data);
            
        });
    };


    angular.extend($scope, {
        searchbox: {
            template:'static/templates/partials/searchbox.html',
            events:{
                places_changed: function (searchBox) {

                }
            }
        },
        options: {
            scrollwheel: false
        }
    });

    GoogleMapApi.then(function(maps) {

        //Get GEO, if not avialable, will use default coord values (Central Park)
        if ($scope.geolocationAvailable) {

            navigator.geolocation.getCurrentPosition(function (position) {

                //Update scope with new values
                $scope.map.center = {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude
                };

                //Submit scope. refresh map, submit new values to map.
                $scope.$apply();

                //download and print Markers
                $scope.GetMarkers();
                

            });

        } else{
            console.log("Geo not available.");
            $scope.GetMarkers();
        }

        $scope.pokemonMarkers = [];
        
    })
}]);