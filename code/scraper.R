# Making CSV from all related items on HDX.
library(RCurl)
library(RJSONIO)

fetchRelated <- function() {
	u = "https://data.hdx.rwlabs.org/api/action/related_list"
	doc = fromJSON(getURL(u))
	for (i in 1:length(doc$result)) {
		d = doc$result
		it <- data.frame(
			view_count = d[[i]]$view_count,
			description = d[[i]]$description,
			title = d[[i]]$title,
			url = d[[i]]$url,
			created = d[[i]]$created,
			image_url = d[[i]]$image_url,
			type = d[[i]]$type,
			id = d[[i]]$id,
			owner_id = d[[i]]$owner_id
			)
		if (i == 1) out <- it
		else out <- rbind(out, it)
	}
	return(out)
}

writeOutput <- function(p = NULL, csv = TRUE, json = TRUE) {
	d = fetchRelated()
	d_sub = d[d$title == "Data Explorer",]
	if (csv) write.csv(d, paste0(p,".csv"), row.names = F)
	if (json) {
		for (i in 1:nrow(d_sub)) {
	    with(d_sub, 
	         it <<- list(
	             view_count = view_count[i],
	             description = description[i],
	             title = title[i],
	             url = url[i],
	             created = created[i],
	             image_url = image_url[i],
	             type = type[i],
	             id = id[i],
	             owner_id = owner_id[i]
	         )
	    )
	    if (i == 1) d_json <- it
	    else d_json <- rbind(d_json, it)
	  }
		sink(paste0(p,".json"))
		cat(toJSON(d_json))
		sink()
	}
}

writeOutput("data/gallery_items")

