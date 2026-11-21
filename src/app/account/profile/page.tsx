'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { User, MapPin, Phone, Mail, Plus, Edit2, Trash2, ShieldCheck, ShoppingBag } from 'lucide-react';

interface Address {
  id: string;
  title: string;
  governorate: string;
  city: string;
  detailed: string;
  isDefault: boolean;
}

export default function CustomerProfilePage() {
  const { t } = useLanguage();

  const [name, setName] = useState('م. أحمد الشناوي');
  const [phone, setPhone] = useState('01012345678');
  const [email, setEmail] = useState('eng.ahmed@example.com');

  const [addresses, setAddresses] = useState<Address[]>([
    {
      id: 'addr-1',
      title: 'مقر الشركة الرئيسي (التجمع)',
      governorate: 'القاهرة',
      city: 'القاهرة الجديدة - التجمع الخامس',
      detailed: 'شارع التسعين الشمالي، مجمع البنوك، مبنى رقم 12',
      isDefault: true,
    },
    {
      id: 'addr-2',
      title: 'فرع المعادي والمخزن',
      governorate: 'القاهرة',
      city: 'المعادي الجديدة',
      detailed: 'شارع النصر، عمارة 45، الدور الأرضي',
      isDefault: false,
    },
  ]);

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Top Banner */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
        <div className="flex items-center gap-3.5">
          <div className="w-14 h-14 rounded-2xl bg-petrol-700 text-white font-black text-2xl flex items-center justify-center shadow-md">
            {name.charAt(0)}
          </div>
          <div>
            <h1 className="text-xl sm:text-2xl font-black text-petrol-900">{name}</h1>
            <p className="text-xs text-slate-500 font-mono">{phone} • {email}</p>
          </div>
        </div>

        <div className="flex items-center gap-2.5">
          <Link
            href="/account/orders"
            className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs shadow-xs transition-colors"
          >
            <ShoppingBag className="w-4 h-4 text-sky-300" />
            <span>سجل طلباتي السابقة</span>
          </Link>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Personal Details */}
        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-5">
          <div className="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 className="font-extrabold text-sm text-petrol-900 flex items-center gap-2">
              <User className="w-4 h-4 text-sky-600" />
              <span>البيانات الشخصية</span>
            </h3>
            <button className="text-[11px] font-bold text-sky-700 hover:underline">تعديل</button>
          </div>

          <div className="space-y-3.5 text-xs">
            <div>
              <span className="text-slate-400 block mb-0.5">الاسم بالكامل:</span>
              <span className="font-bold text-slate-800">{name}</span>
            </div>

            <div>
              <span className="text-slate-400 block mb-0.5">رقم الهاتف (واتساب):</span>
              <span className="font-mono font-bold text-slate-800">{phone}</span>
            </div>

            <div>
              <span className="text-slate-400 block mb-0.5">البريد الإلكتروني:</span>
              <span className="font-mono text-slate-800">{email}</span>
            </div>
          </div>
        </div>

        {/* Address Book */}
        <div className="lg:col-span-2 bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-5">
          <div className="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 className="font-extrabold text-sm text-petrol-900 flex items-center gap-2">
              <MapPin className="w-4 h-4 text-sky-600" />
              <span>دفتر عناوين الشحن والتوصيل</span>
            </h3>
            <button
              onClick={() => alert('إضافة عنوان جديد')}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-petrol-50 text-petrol-800 hover:bg-petrol-100 text-xs font-bold transition-colors"
            >
              <Plus className="w-3.5 h-3.5" />
              <span>عنوان جديد</span>
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {addresses.map((addr) => (
              <div
                key={addr.id}
                className="p-4 rounded-xl border border-slate-200 bg-slate-50/60 hover:bg-white hover:border-petrol-300 transition-all space-y-2 relative"
              >
                <div className="flex items-center justify-between">
                  <h4 className="font-bold text-xs text-petrol-900">{addr.title}</h4>
                  {addr.isDefault && (
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200">
                      افتراضي
                    </span>
                  )}
                </div>

                <p className="text-xs text-slate-600 leading-relaxed">{addr.detailed}</p>
                <span className="text-[11px] text-slate-400 block font-medium">
                  {addr.city}، {addr.governorate}
                </span>

                <div className="pt-2 flex items-center gap-3 border-t border-slate-200 text-xs">
                  <button className="text-sky-700 font-bold hover:underline flex items-center gap-1">
                    <Edit2 className="w-3 h-3" />
                    <span>تعديل</span>
                  </button>
                  <button className="text-rose-600 font-bold hover:underline flex items-center gap-1">
                    <Trash2 className="w-3 h-3" />
                    <span>حذف</span>
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
