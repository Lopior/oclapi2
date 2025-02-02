db.export.sources.drop();
db.export.source_ids.drop();
db.export.sourceversions.drop();
db.export.sourceversion_ids.drop();


org_ids = db.orgs_organization.find({mnemonic: {$in: ["EthiopiaNHDD", "MSFOCP", "Malawi-Demo"]}}, {_id: 1}).map(doc => doc._id.str);
source_ids = db.sources_source.find({parent_id: {$in: org_ids}}, {_id: 1}).map(doc => doc._id.str);

db.export.sources.insertMany(db.sources_source.find({parent_id: {$in: org_ids}}).map(doc => doc));
db.export.sourceversions.insertMany(db.sources_sourceversion.find({versioned_object_id: {$in: source_ids}, mnemonic: {$ne: 'HEAD'}}).map(doc => doc));
db.export.source_ids.insertMany(db.sources_source.find({}).map(doc => ({_id: doc._id, uri: doc.uri})))
db.export.sourceversion_ids.insertMany(db.sources_sourceversion.find({mnemonic: {$ne: 'HEAD'}}).map(doc => ({_id: doc._id, uri: doc.uri})))

print(db.export.sources.count() + " matching source found");
print(db.export.sourceversions.count() + " matching sourceversion found");