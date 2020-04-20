# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class L0FitsCommonMetadata(models.Model):
    l0_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=255)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    obt_end = models.FloatField(blank=True, null=True)
    obt_beg = models.FloatField(blank=True, null=True)
    compress = models.CharField(max_length=255, blank=True, null=True)
    comp_ratio = models.IntegerField(blank=True, null=True)
    hdr_version = models.IntegerField(blank=True, null=True)
    datatytpe = models.IntegerField()
    obj_count = models.IntegerField(blank=True, null=True)
    conf_id = models.IntegerField(blank=True, null=True)
    sess_num = models.IntegerField(blank=True, null=True)
    compr = models.NullBooleanField()
    radial = models.NullBooleanField()
    cadence = models.IntegerField(blank=True, null=True)
    cad_beg = models.CharField(max_length=255, blank=True, null=True)
    cad_end = models.CharField(max_length=255, blank=True, null=True)
    apid = models.IntegerField(blank=True, null=True)
    masking = models.NullBooleanField()
    mask_rmin = models.IntegerField(blank=True, null=True)
    mask_rmax = models.IntegerField(blank=True, null=True)
    naxis = models.IntegerField(blank=True, null=True)
    naxi1 = models.IntegerField(blank=True, null=True)
    naxis2 = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    vers_sw = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    history = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    tsensor = models.IntegerField(blank=True, null=True)
    vl_image = models.ForeignKey('VlImage', models.DO_NOTHING, unique=True, blank=True, null=True)
    uv_image_id = models.IntegerField(blank=True, null=True)
    vl_cr_log_mat_id = models.IntegerField(blank=True, null=True)
    light_curve_id = models.IntegerField(blank=True, null=True)
    uv_cr_log_mat_id = models.IntegerField(blank=True, null=True)
    vl_temp_mat_id = models.IntegerField(blank=True, null=True)
    uv_temp_mat_id = models.IntegerField(blank=True, null=True)
    pcu_event_list_id = models.IntegerField(blank=True, null=True)
    pcu_event_acc_mat_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l0_fits_common_metadata'


class VlImage(models.Model):
    vl_image_id = models.IntegerField(primary_key=True)
    pol_id = models.IntegerField(blank=True, null=True)
    measkind = models.NullBooleanField()
    framemod = models.NullBooleanField()
    vlfpfilt = models.IntegerField(blank=True, null=True)
    cr_sep = models.NullBooleanField()
    cme_obs = models.NullBooleanField()
    sun_disk = models.NullBooleanField()
    sp_noise = models.NullBooleanField()
    pmpstab = models.NullBooleanField()
    ref_rows = models.NullBooleanField()
    ndit = models.IntegerField(blank=True, null=True)
    snr_min = models.IntegerField(blank=True, null=True)
    snr_max = models.IntegerField(blank=True, null=True)
    dac1pol1 = models.IntegerField(blank=True, null=True)
    dac1pol2 = models.IntegerField(blank=True, null=True)
    daclpol3 = models.IntegerField(blank=True, null=True)
    dac1pol4 = models.IntegerField(blank=True, null=True)
    dac2pol1 = models.IntegerField(blank=True, null=True)
    dac2pol2 = models.IntegerField(blank=True, null=True)
    dac2pol3 = models.IntegerField(blank=True, null=True)
    dac2pol4 = models.IntegerField(blank=True, null=True)
    pmptemp = models.IntegerField(blank=True, null=True)
    nb_img = models.IntegerField(blank=True, null=True)
    cr_sep_a = models.FloatField(blank=True, null=True)
    cr_sep_b = models.FloatField(blank=True, null=True)
    dit = models.IntegerField(blank=True, null=True)
    npol = models.IntegerField(blank=True, null=True)
    nseq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vl_image'
