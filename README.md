# ga4gh-mongo

A document based Variant database inspired by ga4gh Variants schema.

https://github.com/ga4gh/schemas

## Usage

	from ga4ghmongo.schema import Variant
	v = Variant.create(start=0,reference_bases="A", alternate_bases=["T"])
	v.to_mongo().to_dict()
	
	{'info': {}, 'is_snp': True, 'is_insertion': False, 'reference_bases': u'A', 'created_at': datetime.datetime(2016, 3, 16, 15, 11, 43, 989088), 'updated_at': datetime.datetime(2016, 3, 16, 15, 11, 43, 989189), 'start': 0, 'var_hash': u'b819f0202b6a9dff2821bbcf7dac87536bc9cb08be6eb96c8dad3fd4fd2a6fd6', 'names': [u'A0T'], 'is_indel': False, 'length': 0, 'alternate_bases': [u'T'], 'is_deletion': False, 'variant_sets': []}

### Changes from ga4gh v0.5.1 API

*	In ga4gh schema each Variant must belong to one and only one VariantSet. Here we allow Variants to belong to multiple VariantSets


 