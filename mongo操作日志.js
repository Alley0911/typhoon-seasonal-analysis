rs.initiate({
	"_id":"sh1",
	"members":[
		{"_id":0, "host":"127.0.0.1:27016", "priority":3},
		{"_id":1, "host":"127.0.0.1:27018", "priority":1},
		{"_id":2, "host":"127.0.0.1:27019", "arbiterOnly":true},
		]
	})

rs.initiate({
	"_id":"sh2",
	"members":[
		{"_id":0, "host":"127.0.0.1:27117", "priority":3},
		{"_id":1, "host":"127.0.0.1:27118", "priority":1},
		{"_id":2, "host":"127.0.0.1:27119", "arbiterOnly":true},
		]
	})

rs.initiate({
	"_id":"cfs",
	"members":[
		{"_id":0, "host":"127.0.0.1:27217", "priority":3},
		{"_id":1, "host":"127.0.0.1:27218", "priority":1},
		{"_id":2, "host":"127.0.0.1:27219", "priority":1},
		]
	})

// mongos加shard
// 需要useadmin
sh.addShard("sh1/127.0.0.1:27017,127.0.0.1:27018,127.0.0.1:27019")
一样的
db.runCommand({"addShard":"sh1/127.0.0.1:27017,127.0.0.1:27018,127.0.0.1:27019"})
db.runCommand({"addShard":"sh2/127.0.0.1:27117,127.0.0.1:27118,127.0.0.1:27119"})

// 开启tysn数据库分片功能
sh.enablesharding("tysn")
// 开启tysn数据库下era5集合的分片功能
sh.shardCollection("tysa.era5", {"_id":"hashed"})
或
db.runCommand({"enablesharding":"tysa"})
db.runCommand({"shardcollection":"tysa.era5", "key":{"loc":"hashed"}})


// 分片信息查询
sh.status()

// 500hPa位势高度场，1981-2019月平均，json13.38gb大小，插入后4.6gb大小
// mongonimport插入数据耗时9m45.180s
// grib转成json耗时900多秒

db.era5.find({"loc.coordinates":[0.5,90]}) // 耗时大概30s


// 使用GridFS
mongofiles -d gribfs put gh_500_*