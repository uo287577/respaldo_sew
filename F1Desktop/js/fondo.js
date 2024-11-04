/* Miguel Fernández Huerta UO287577 */

"use strict";
class Fondo
{
    constructor(nombrePais,nombreCapital,nombreCircuito)
    {
        this.nombrePais = nombrePais;
        this.nombreCapital = nombreCapital;
        this.nombreCircuito = nombreCircuito;
    }

    getImagenFondo()
    {
        (function()
        {
            // metodo a usar: flickr.photos.geo.photosForLocation
            // link del metodo a usar: https://www.flickr.com/services/api/flickr.photos.geo.photosForLocation.html
            //https://www.flickr.com/services/rest/?method=flickr.photos.geo.photosForLocation&api_key=41548d55ff86ff444bdb7fe25960e91a&lat=41.564792&lon=2.261216&accuracy=11&format=json&nojsoncallback=1&auth_token=72157720933126896-43261d60fabfec95&api_sig=37fd1f9cbd7019d848dcbd255ba3ef3c

            var flickrAPI = "https://www.flickr.com/services/rest/";
            $.getJSON(flickrAPI,
                {
                    method: "flickr.photos.geo.photosForLocation",
                    tags: this.nombrePais + " " + this.nombreCircuito,
                    api_key: "8cd3e5ea29ea8f760d938f32acb9bc75",
                    tagmode: "all",
                    format: "json"
                })
            .done(function(data) 
            {
                $.each(data.items, function(i,item)
                {
                    $("<img />").attr("src", item.media.m).appendTo("body > main");
                    if( i === 1 )
                    {
                        return false;
                    }
                })
            })
        })();
    }
}